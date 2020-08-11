import { createStore, applyMiddleware } from 'redux';
import { composeWithDevTools} from 'redux-devtools-extension';
import thunk from 'redux-thunk'; // https://github.com/reduxjs/redux-thunk
import rootReducer from './reducers'; // looks for a file named index.js inside the reducers folder, imports the default exported combineReducers()
                                      // - default exports can be named anything when imported: https://developer.mozilla.org/en-US/docs/web/javascript/reference/statements/export

const initialState = {};

const middleware = [thunk];

// rootReducer - imported above, "a meeting place for all of your other reducers"
const store = createStore(
  rootReducer, 
  initialState,
  composeWithDevTools(applyMiddleware(...middleware))
);
// spread operator ... - takes each element of an iterable separately (also, it can be used to copy an object into a new object: https://medium.com/technofunnel/working-with-react-pure-components-166ded26ae48 - "If we want to copy the object into a new object, we can use the spread operator."")
// Ex) const numbers = [1, 2, 3]; sum(...numbers) -> output: 6

export default store;
