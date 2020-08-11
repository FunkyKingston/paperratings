import axios from 'axios';

import { GET_PAPERS, GET_PAPER, DELETE_PAPER, ADD_PAPER } from './types';

// GET PAPERS
export const getPapers = () => dispatch => {
  axios
    .get('/api/papers/')
    .then(res => {
      dispatch({
        // in the reducer, the action.type is evaluated
        type: GET_PAPERS,
        payload: res.data
      })
    })
    .catch(err => console.log(err));
};

// GET PAPER
export const getPaper = (id) => dispatch => {
  axios
    .get(`/api/papers/${id}/`)
    .then(res => {
      dispatch({
        type: GET_PAPER,
        payload: res.data
      })
    })
    .catch(err => console.log(err));
};

// DELETE PAPER
export const deletePaper = (id) => dispatch => {
  axios
    .delete(`/api/papers/${id}/`)
    .then(res => {
      dispatch({
        type: DELETE_PAPER,
        payload: id
      })
    })
    .catch(err => console.log(err));
};

// EDIT PAPER


// ADD PAPER
export const addPaper = (paper) => dispatch => {
  console.log(paper) 
  axios
    .post("/api/papers/", paper)
    .then(res => {
      dispatch({
        type: ADD_PAPER,
        payload: res.data // res - the response from the server, includes auto-generated paper id (primary key in Paper table)
      })
    })
    .catch(err => console.log(err.response)); // contains err.response.data field
};


