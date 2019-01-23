#include "predict.hpp"
#include <cmath>
#include <cassert>
#include <stack>
#include "util.hpp"
//
//Implemented TODO parts by Jayden Caelli (u5564556)
//
CTNode::CTNode(void) :
	m_log_prob_est(0.0),
	m_log_prob_weighted(0.0)
{

	m_count[0] = 0;
	m_count[1] = 0;
	m_child[0] = NULL;
	m_child[1] = NULL;
}


CTNode::~CTNode(void) {

	if (m_child[0]) delete m_child[0];
	if (m_child[1]) delete m_child[1];
}


// number of descendants of a node in the context tree
size_t CTNode::size(void) const {

    size_t rval = 1;
    rval += child(false) ? child(false)->size() : 0;
    rval += child(true)  ? child(true)->size()  : 0;
    return rval;
}


// compute the logarithm of the KT-estimator update multiplier
double CTNode::logKTMul(symbol_t sym) const {

	double kTMulNum = std::log(double(m_count[sym]) + 0.5);
	double kTMulDom = std::log(double(m_count[true]) + double(m_count[false]) + 1.0);
	return (kTMulNum - kTMulDom);
}

// Calculate the logarithm of the weighted block probability.
// Calculates the block probability as specifed by using the
//fomula:
// log Pw = log Pkt	if a leaf
// log Pw = log(0.5) + e^(logPkt) + e^(log(Pw0) + log(Pw1)) else
void CTNode::updateLogProbability(void) {

	if (m_child[true] == NULL && m_child[false] == NULL){
		m_log_prob_weighted = m_log_prob_est;
	}else{
		 double left_child_p = 0.0;
		 double right_child_p = 0.0;
		 if (m_child[true]){
		 	left_child_p = m_child[true]->m_log_prob_weighted;
		 }
		 if (m_child[false]){
		 	right_child_p = m_child[false]->m_log_prob_weighted;
		 }
        double log_half = std::log(0.5);
		 m_log_prob_weighted = log_half + std::log(exp(m_log_prob_est) + exp(left_child_p + right_child_p));
	}
}

// Update the node after having observed a new symbol.
// recalculates the logKTMul for the symbol, updates
// the block probability and adds one to the symbol count.
void CTNode::update(const symbol_t symbol){
	m_log_prob_est += logKTMul(symbol);
	updateLogProbability();
	m_count[symbol]++;
}

//Reverts the node by reducing the count of the symbol
//And recalculating the KT Multiplier and log probability.
void CTNode::revert(const symbol_t symbol){
	m_count[symbol]--;
	if (m_child[symbol] && m_count[symbol] == 0) {
		delete m_child[symbol];
		m_child[symbol] = NULL;
	}
	m_log_prob_est -= logKTMul(symbol);
	updateLogProbability();
}

// create a context tree of specified maximum depth
ContextTree::ContextTree(size_t depth) :
	m_root(new CTNode()), m_depth(depth)
{
	m_history_node = new CTNode*[m_depth + 1];
	return;
}


ContextTree::~ContextTree(void) {
	m_history.clear();
	delete[] m_history_node;
	if (m_root) delete m_root;
}

// clear the entire context tree
void ContextTree::clear(void) {
	m_history.clear();
	if (m_root) delete m_root;
	m_root = new CTNode();
}

//Updates the context tree with a specifed symbol.
//Does this by following the context from the root
//down as far as possible. If the node specified by
//the context doesn't exist, then create it.
void ContextTree::update(const symbol_t sym) {
	if (m_history.size() >= m_depth) {
		updateContext();
		for (int i = m_depth; i >= 0; i--) {
			m_history_node[i]->update(sym);
		}
	}
	updateHistory(sym);
}

// tree with each bit
void ContextTree::update(const symbol_list_t &symbol_list) {
    for (size_t i = 0; i < symbol_list.size(); i++){
        update(symbol_list[i]);
    }
}

// updates the history statistics, without touching the context tree
void ContextTree::updateHistory(const symbol_t symbol) {
	m_history.push_back(symbol);
}

// updates the history statistics, without touching the context tree
void ContextTree::updateHistory(const symbol_list_t &symbol_list) {
    for (size_t i=0; i < symbol_list.size(); i++) {
        updateHistory(symbol_list[i]);
    }
}

// removes the most recently observed symbol from the context tree
// Follows a path from the root to a leaf node based on the stored context
// (last depth bits of history)
// Then calls revert on each node from the leaf to the root based on the last
// updated symbol (last symbol in the history)
void ContextTree::revert(void) {
	// No updates to revert // TODO: maybe this should be an assertion?
	if (m_history.size() == 0)
		return;

	// Get the most recent symbol and delete from history
	const symbol_t symbol = m_history.back();
	m_history.pop_back();

	// Traverse the tree from leaf to root according to the context. Update the
	// probabilities and symbol counts for each node. Delete unnecessary nodes.
	if (m_history.size() >= m_depth) {
		updateContext();
		for (int i = m_depth; i >= 0; i--) {
			m_history_node[i]->revert(symbol);
		}
	}
}

void ContextTree::revert(size_t num_symbols) {
	for(int i = 0; i < num_symbols; i++) {
		revert();
	}
}

// revert a bit history
void ContextTree::revertHistory() {
    m_history.pop_back();
}

// revert bits history
void ContextTree::revertHistory(size_t num_bits) {
    assert(num_bits <= m_history.size());
    for(int i = 0; i < num_bits; i++) {
        revertHistory();
    }
}



// generate a specified number of random symbols
// distributed according to the context tree statistics
void ContextTree::genRandomSymbols(symbol_list_t &symbols, size_t bits) {

	genRandomSymbolsAndUpdate(symbols, bits);
	revert(bits);
}


// generate a specified number of random symbols distributed according to
// the context tree statistics and update the context tree with the newly
// generated bits
void ContextTree::genRandomSymbolsAndUpdate(symbol_list_t &symbols, size_t bits) {
	symbols.resize(bits);

	for (int i = 0; i < bits; i++){
		symbols[i] = rand01() < predict(true);
		update(symbols[i]);
	}
}

// the logarithm of the block probability of the whole sequence
double ContextTree::logBlockProbability(void) {
	return m_root->logProbWeighted();
}

// Returns the predicted probability of the next
// symbol being sym based on the observed history.
// Calculates logP(s | H) = log p(s AND H)) - log P(h)
double ContextTree::predict(symbol_t const sym){
	//If there is not enough history + 1 (sym) then
	//return uniform probability of 0.5
	if (m_history.size() + 1 < m_depth){
		return 0.5;
	}
	weight_t prob_of_hist = logBlockProbability();  // log P(H)
	update(sym);
	weight_t prob_sym_and_hist = logBlockProbability(); // log P(sym AND H)
	revert();
	return std::exp((double) prob_sym_and_hist - (double) prob_of_hist);
}


// Returns the predicted probability of the next
// n (size of sym) symbols being sym based on the
// pbserved history.
// Calculates logP(s | H) = log p(s AND H)) - log P(h)
double ContextTree::predict(symbol_list_t sym){
	//prediction then return a uniform probability.
	if (m_history.size() + sym.size() <= m_depth){
		return pow(0.5, (int) sym.size());
	}
	weight_t prob_of_hist = logBlockProbability(); // logP(H)
	update(sym);
	weight_t prob_sym_and_hist = logBlockProbability(); //log P(s AND H)
	for (size_t i = 0; i < sym.size(); i++){
		revert();
	}
	return std::exp(prob_sym_and_hist - prob_of_hist);
}

// get the n'th most recent history symbol, NULL if doesn't exist
const symbol_t *ContextTree::nthHistorySymbol(size_t n) const {
    return n < m_history.size() ? &m_history[n] : NULL;
}

// Get the nodes in the current context
void ContextTree::updateContext(void) {
	assert(m_history.size() >= m_depth);
	m_history_node[0] = m_root;
	CTNode **node = &m_root;
	history_t::reverse_iterator symbol_iter = m_history.rbegin();
	for (int i = 1; i <= m_depth; symbol_iter++, i++) {
		node = &((*node)->m_child[*symbol_iter]);
		if (*node == NULL)
			*node = new CTNode();
		m_history_node[i] = *node;
	}
}