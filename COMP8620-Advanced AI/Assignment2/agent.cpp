#include <cassert>
#include <iostream>

#include "agent.hpp"
#include "predict.hpp"
#include "search.hpp"
#include "util.hpp"

// construct a learning agent from the command line arguments
Agent::Agent(options_t & options) {
	std::string s;

	strExtract(options["agent-actions"], m_actions);
	strExtract(options["agent-horizon"], m_horizon);
	strExtract(options["observation-bits"], m_obs_bits);
	strExtract<unsigned int>(options["reward-bits"], m_rew_bits);
	strExtract(options["mc-simulations"], m_mc_simulations);


	// calculate the number of bits needed to represent the action
	for (unsigned int i = 1, c = 1; i < m_actions; i *= 2, c++) {
		m_actions_bits = c;
	}

	m_ct = new ContextTree(strExtract<unsigned int>(options["ct-depth"]));

	reset();
}


// destroy the agent and the corresponding context tree
Agent::~Agent() {
	if (m_ct) delete m_ct;
}

// current lifetime of the agent in cycles
lifetime_t Agent::lifetime() const {
	return m_time_cycle;
}

bool Agent::lastUpdatePercept(void) const{
	return m_last_update_percept;
}

// maximum reward
reward_t Agent::maxReward() const {
	return reward_t((1 << m_rew_bits) - 1);
}

// minimum reward in a single time instant
reward_t Agent::minReward() const {
	return 0.0;
}

// the total accumulated reward across an agents lifespan
reward_t Agent::reward() const {
    return m_total_reward;
}

// the average reward received by the agent at each time step
reward_t Agent::averageReward() const {
	return lifetime() > 0 ? reward() / reward_t(lifetime()) : 0.0;
}

// number of distinct actions
unsigned int Agent::numActions() const {
	return m_actions;
}

// the length of the stored history for an agent
size_t Agent::historySize() const {
	return m_ct->historySize();
}

// length of the search horizon used by the agent
size_t Agent::horizon() const {
	return m_horizon;
}

// generate an action uniformly at random
action_t Agent::genRandomAction() const {
	return randRange(m_actions);
}

// generate a percept distributed to our history statistics, and
// update our mixture environment model with it
void Agent::genPerceptAndUpdate(percept_t &o, percept_t &r) {
	assert(!m_last_update_percept);
	symbol_list_t obs_syms, rew_syms;
    m_ct->genRandomSymbolsAndUpdate(obs_syms, m_obs_bits);
    m_ct->genRandomSymbolsAndUpdate(rew_syms, m_rew_bits);
    o = decodeObservation(obs_syms);
    r = decodeReward(rew_syms);
	assert(isRewardOk(r));
	m_total_reward += r;
	m_last_update_percept = true;
}

// Update the agent's internal model of the world after receiving a percept
void Agent::modelUpdate(percept_t observation, percept_t reward) {
	assert(!m_last_update_percept);
	// Update internal model
	symbol_list_t percept_syms;
	encodePercept(percept_syms, observation, reward);
	m_ct->update(percept_syms);

	// Update other properties
	m_total_reward += reward;
	m_last_update_percept = true;
}


// Update the agent's internal model of the world after performing an action
void Agent::modelUpdate(const action_t action) {
	assert(isActionOk(action));
	assert(m_last_update_percept);

	// Update internal model
	symbol_list_t action_syms;
	encodeAction(action_syms, action);
	m_ct->updateHistory(action_syms);

	m_time_cycle++;
	m_last_update_percept = false;
}


// revert the agent's internal model of the world
// to that of a previous time cycle
void Agent::modelRevert(const ModelUndo &mu) {
	assert(lifetime() > mu.lifetime());
	while (historySize() > mu.historySize()) {
        if (m_last_update_percept) {
            m_ct->revert(m_rew_bits + m_obs_bits);
            m_last_update_percept = false;
        }
        else{
            m_ct->revertHistory(m_actions_bits);
            m_last_update_percept = true;
        }
	}
	m_time_cycle = mu.lifetime();
	m_total_reward = mu.reward();
    m_last_update_percept = mu.lastUpdate();
}


void Agent::reset() {
	m_ct->clear();
	m_time_cycle = 0;
	m_total_reward = 0.0;
	m_last_update_percept = false;
}


// probability of selecting an action according to the
// agent's internal model of it's own behaviour
double Agent::getPredictedActionProb(const action_t action) {
	assert(m_last_update_percept);
	symbol_list_t action_syms;
	encodeAction(action_syms, action);
	return m_ct->predict(action_syms);
}


// get the agent's probability of receiving a particular percept
double Agent::perceptProbability(const percept_t observation, const percept_t reward) const {
	assert(!m_last_update_percept);
	symbol_list_t percept;
	encodePercept(percept, observation, reward);
	return m_ct->predict(percept);
}

// action sanity check
bool Agent::isActionOk(action_t action) const {
	return action < m_actions;
}


// reward sanity check
bool Agent::isRewardOk(reward_t reward) const {
    return reward >= minReward() && reward <= maxReward();
}

// Encodes an action as a list of symbols
void Agent::encodeAction(symbol_list_t &symlist, action_t action) const {
	symlist.clear();
	encode(symlist, action, m_actions_bits);
}

// Encodes a percept (observation, reward) as a list of symbols
void Agent::encodePercept(symbol_list_t &symlist, percept_t observation, percept_t reward) const {
	symlist.clear();
    encode(symlist, observation, m_obs_bits);
    encode(symlist, reward, m_rew_bits);
}

// Decodes the observation from a list of symbols
action_t Agent::decodeAction(const symbol_list_t &symlist) const {
	return decode(symlist, m_actions_bits);
}

// Decodes the reward from a list of symbols
percept_t Agent::decodeReward(const symbol_list_t &symlist) const {
	return decode(symlist, m_rew_bits);
}

// Decodes the observation from a list of symbols
percept_t Agent::decodeObservation(const symbol_list_t &symlist) const {
	return decode(symlist, m_obs_bits);
}

// used to revert an agent to a previous state
ModelUndo::ModelUndo(const Agent &agent) {
	m_lifetime     = agent.lifetime();
    m_reward       = agent.reward();
    m_history_size = agent.historySize();
	m_last_update_percept = agent.lastUpdatePercept();
}
