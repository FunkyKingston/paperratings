import axios from 'axios';

import { GET_COMMENTS, DELETE_COMMENT, EDIT_COMMENT, ADD_COMMENT } from './types';

// GET COMMENTS
export const getComments = (paper_id) => dispatch => {
  axios
    .get(`/api/commentlistbypaper?paper_id=${paper_id}`)
    .then(res => {
      dispatch({
        type: GET_COMMENTS,
        payload: res.data
      })
    })
    .catch(err => console.log(err));
};

// GET COMMENT


// DELETE COMMENT
export const deleteComment = (id) => dispatch => {
  axios
    .delete(`/api/comments/${id}/`)
    .then(res => {
      dispatch({
        type: DELETE_COMMENT,
        payload: id
      })
    })
    .catch(err => console.log(err));
};

// EDIT COMMENT - input comment including comment.id (unlike for ADD COMMENT which creates the id at the backend)
export const editComment = (comment) => (dispatch, getState) => {
  axios
    .put(`/api/comments/${comment.id}/`, comment)
    .then(res => {
      const user_data = getState().auth.user;
      dispatch({
        type: EDIT_COMMENT,
        // payload: res.data // res - the response from the server, in the format of CommentSerializer
        payload: {id: res.data.id, text: res.data.text, time: res.data.time, user_data: user_data} // comment format of the CommentDetailsSerializer instead of CommentSerializer, papers.api CommentListByPaper class
      })
    })
    .catch(err => console.log(err));
};

// ADD COMMENT
export const addComment = (comment) => (dispatch, getState) => {
  axios
    .post("/api/comments/", comment)
    .then(res => {
      const user_data = getState().auth.user;
      dispatch({
        type: ADD_COMMENT,
        // payload: res.data // res - the response from the server, in the format of CommentSerializer
        payload: {id: res.data.id, text: res.data.text, time: res.data.time, user_data: user_data} // comment format of the CommentDetailsSerializer instead of CommentSerializer, papers.api CommentListByPaper class
      })
    })
    .catch(err => console.log(`catch is called with err.response: ${err.response}`)); // contains err.response.data field
};



