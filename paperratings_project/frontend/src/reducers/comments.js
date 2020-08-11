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
      // CHANGING TO CommentDetailsSerializer -> need to store data in the comments state that differs from the action.payload, try out below
      console.log("ADD_COMMENT - action.payload:")
      console.log(action.payload)
      // const newComment = {id: action.payload.id, text: action.payload.text, time: action.payload.time} //, user_data: ...auth.user}
      // const newComment = {...action.payload}
      // const newComment = {...state.auth.user} // njet, state here only includes the state elements for the comments-reducers
      /* -> https://redux.js.org/faq/reducers - " How do I share state between two reducers? Do I have to use combineReducers? "
        kan använda getState kanske? har ju iaf med "thunk" som middleware passed to createStore() (i store.js)
      */

      // const newComment = {...action.payload, user_data: state.auth.user}
      // console.log("newComment in comment.js reducer:")
      // console.log(newComment);
      // 
      return {
        ...state,
        comments: [...state.comments, action.payload]
      }  
    default:
      return state;
  }
}