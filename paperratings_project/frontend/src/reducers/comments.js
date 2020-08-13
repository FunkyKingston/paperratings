import { GET_COMMENTS, DELETE_COMMENT, EDIT_COMMENT, ADD_COMMENT } from '../actions/types.js';

const initialState = {
  comments: [] 
}

// dispatched [comments] actions are handled by the [comments] reducer
export default function(state = initialState, action) {
  switch(action.type) {
    case GET_COMMENTS:
      return {
        ...state, 
        comments: action.payload 
      }
    case DELETE_COMMENT:
      return {
        ...state,
        comments: state.comments.filter(comment => comment.id != action.payload) // for this case action.payload is only an id, not the full comment object
      }
    case EDIT_COMMENT: // https://medium.com/javascript-in-plain-english/react-updating-a-value-in-state-array-7bae7c7eaef9
      const elementIndex = state.comments.findIndex(comment => comment.id == action.payload.id );
      let newComments = [...state.comments];
      newComments[elementIndex] = action.payload;
      // console.log(newComments);
      return {
        ...state,
        comments: newComments
      }
    case ADD_COMMENT:
      // console.log("ADD_COMMENT - action.payload:")
      // console.log(action.payload)
      return {
        ...state,
        comments: [...state.comments, action.payload]
      }  
    default:
      return state;
  }
}