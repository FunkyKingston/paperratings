import React, { Component } from 'react';
import ReactDOM from 'react-dom';

import Header from './layout/Header';
import Footer from './layout/Footer';
import Login from './accounts/Login';
import Register from './accounts/Register';
import PrivateRoute from './common/PrivateRoute';


import Papers from './papers/Papers';

import PaperDetails from './papers/PaperDetails';
import About from './papers/About';
import Profile from './accounts/Profile';
import MyPapers from './accounts/MyPapers';

import { Provider } from 'react-redux'; // to make store globally available to all the components wrapped by the Provider
import store from '../store';
import { loadUser } from '../actions/auth';

// Redux - usage with React Router: https://redux.js.org/advanced/usage-with-react-router
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
//import { HashRouter as Router, Switch, Route } from 'react-router-dom';


class App extends Component {
  componentDidMount() {
    store.dispatch(loadUser());
    // console.log("ran componentDidMount() in App.js...")
  }

  render() {
    return (
      <Provider store={store}>
        <Router>

          <div className="wrapper">
            <Header />
            {/* <div className="logo-img"></div> */}

            <div className="content-wrapper">
              
              <Switch>
                <Route exact path="/" component={Papers} /> {/* "/" -> welcome page w. "highlighted" search form - redirects to "/search?xxx=yyy&..." */}
                <Route path="/paper/:id" component={PaperDetails} />
                <Route exact path="/about" component={About} />
                <Route exact path="/join" component={Register} />
                <Route exact path="/login" component={Login} />
                <PrivateRoute exact path="/profile" component={Profile} />
                <PrivateRoute exact path="/mypapers" component={MyPapers} />
              </Switch>

            </div> 

            <Footer />
          </div>

        </Router>  
      </Provider>
    )
  }
}


ReactDOM.render(<App />, document.getElementById('app'));