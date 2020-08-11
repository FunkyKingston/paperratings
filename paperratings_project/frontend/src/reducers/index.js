import { combineReducers } from 'redux';
import auth from './auth';
import papers from './papers';
import comments from './comments';
//import userPapers from './userPapers';

export default combineReducers({
  papers,
  comments,
  //userPapers,
  auth
});
