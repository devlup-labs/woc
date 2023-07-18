import {httpClient} from '../../plugins/httpClient'

const state = {
  proposalList: [
    /* {
    id: '',
    project: '',
    student: '',
    drive_link: '',
    file: null,
    proposalStatus: false
  } */
  ]
}

const getters = {
  proposalList: (state, getters) => state.proposalList[0] ? state.proposalList : [],
  studentProposalList: (state, getters, rootState, rootGetters) => state.proposalList
    .filter(proposal => proposal.student === rootGetters['studentProfile/studentProfile'].id)
}

const mutations = {
  'SET_PROPOSAL_LIST' (state, proposalList) {
    state.proposalList = proposalList
  },
  'REMOVE_PROPOSAL' (state, proposalId) {
    state.proposalList = state.proposalList.filter(proposal => proposal.id !== proposalId)
  },
  'ADD_PROPOSAL' (state, proposal) {
    state.proposalList.push(proposal)
  },
  'UPDATE_PROPOSAL' (state, updatedProposal) {
    state.proposalList = [
      ...state.proposalList.filter(proposal => proposal.id !== updatedProposal.id),
      updatedProposal
    ].sort((a, b) => a.id - b.id)
  }
}

const actions = {
  fetchProposalList ({commit}, state) {
    httpClient.get('/api/project/student-proposal/').then(response => {
      commit('SET_PROPOSAL_LIST', response.data)
    }).catch(err => console.log(err))
  },
  removeProposalById ({commit}, proposalId) {
    commit('REMOVE_PROPOSAL', proposalId)
  },
  addProposal ({commit}, proposal) {
    commit('ADD_PROPOSAL', proposal)
  },
  updateProposal ({commit}, proposal) {
    commit('UPDATE_PROPOSAL', proposal)
  }
}

export {
  state,
  getters,
  mutations,
  actions
}
