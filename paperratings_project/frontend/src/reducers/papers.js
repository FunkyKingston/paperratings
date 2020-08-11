import { GET_PAPERS, GET_PAPER, DELETE_PAPER, ADD_PAPER } from '../actions/types.js';

const initialState = {
  papers: [],
  currentPaper: {}
}

// actions are dispatched to the reducer
export default function(state = initialState, action) {
  switch(action.type) {
    case GET_PAPERS:
      return {
        ...state, 
        papers: action.payload // make sure to send as payload of the action for this action.type
      }
    case GET_PAPER:
      return {
        ...state,
        currentPaper: action.payload
      }
    case DELETE_PAPER:
      return {
        ...state,
        papers: state.papers.filter(paper => paper.id != action.payload)
      }
    case ADD_PAPER:
      return {
        ...state,
        papers: [...state.papers, action.payload]
      }
    // case EDIT_PAPER:
    //   return {}
    default:
      return state;
  }
}