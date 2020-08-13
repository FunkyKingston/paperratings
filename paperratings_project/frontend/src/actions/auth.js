import axios from 'axios'; 

import {
  USER_LOADING,
  USER_LOADED,
  AUTH_ERROR,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT_SUCCESS,
  REGISTER_SUCCESS,
  REGISTER_FAIL
} from './types';

// about dispatching actions in redux ("pass the result to the dispatch() function"): https://redux.js.org/basics/actions

// CHECK TOKEN & LOAD USER
export const loadUser = () => (dispatch, getState) => { // called in App.js during componentDidMount() { store.dispatch(loadUser()); }
  // User Loading
  dispatch({ type: USER_LOADING });

  // Header data is set up by tokenConfig(getState), getting token from redux state and returns config
  axios.get('/api/auth/user', tokenConfig(getState)) 
    .then(res=> {
      // console.log('/api/auth/user called - res.data:')
      // console.log(res.data)
      dispatch({
        type: USER_LOADED,
        payload: res.data
      });
    }).catch(err => {
      // console.log("loadUser err.response:")
      // console.log(err.response)
      /*
        TO DO (for this as well as all other actions):
        1. dispatch returnErrors, not implemented yet - https://www.youtube.com/watch?v=Fia-GGgHpK0&list=PLillGF-RfqbbRA-CIUxlxkUpbq0IFkX60&index=4
        2.
      */ 
      dispatch({
        type: AUTH_ERROR
      });
    });
}


// LOGIN USER
export const login = (username, password) => dispatch => {
  // Headers
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  };

  // Request Body (turn into json object)
  const body = JSON.stringify({ username, password }); // <=> username: username, password: password

  axios.post('/api/auth/login', body, config)
    .then(res=> {
      // console.log('/api/auth/login called - res.data:')
      // console.log(res.data) // the response from the Django API
      dispatch({
        type: LOGIN_SUCCESS,
        payload: res.data
      });
    }).catch(err => {
      // console.log(err.response) // NOTE: err.response exposes the unencrypted password that was entered!!
      // - btw, the error occasionally given by Chrome (in Django local Debug mode), "A data breach on a site or app exposed your password. Chrome recommends changing ..." 
      //   - seems to be (press the information button on the popup!) just a warning based on that I entered a dummy password such as "asdf", which matches passwords in generic password databases that chrome checks against
      dispatch({
        type: LOGIN_FAIL
      });
    });
}


// REGISTER USER
export const register = ({ username, password, email }) => dispatch => {
  // Headers
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  };

  // Request Body (turn into json object)
  const body = JSON.stringify({ username, password, email }); // <=> username: username, password: password

  axios.post('/api/auth/register', body, config)
    .then(res=> {
      dispatch({
        type: REGISTER_SUCCESS,
        payload: res.data
      });
    }).catch(err => {
      console.log(err.response)
      dispatch({
        type: REGISTER_FAIL
      });
    });
}


// LOGOUT USER - note, getState is a redux function, available ... everywhere (? eh, where exactly) when using redux?
export const logout = () => (dispatch, getState) => {
  
  axios.post('/api/auth/logout/', null, tokenConfig(getState)) // body of null needs to be passed in, tokenConfig(getState) gets token from state and returns config
    .then(res=> {
      dispatch({
        type: LOGOUT_SUCCESS
      });
    }).catch(err => {
      console.log(err.response)
    });
}


// Setup config with token - helper function
export const tokenConfig = getState => {
  // Get token from state - getState(): https://redux.js.org/api/store#getstate
  const token = getState().auth.token; // the auth reducer sets localStorage.getItem('token') to redux initialState - i.e., reading from the browser's localStorage when entering to the page, and adding the auth token to the redux state

  // Headers
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  };

  // If token exists, add it to the header
  if(token) {
    config.headers['Authorization'] = `Token ${token}`
  }

  return config;

};