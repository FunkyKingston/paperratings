import React, { Component } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { login } from '../../actions/auth';


export class Login extends Component {
  // "component-level state, has nothing to do with redux" -  - https://spin.atomicobject.com/2017/06/07/react-state-vs-redux-state/#:~:text=Redux%20manages%20state%20and%20state,data%20is%20stored%20in%20Redux.
  state = {
    username: '',
    password: '',
  };

  
  static propTypes = {
    login: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool
  }
  

  onSubmit = e => {
    e.preventDefault();
    // console.log('Login onSubmit function called...')
    this.props.login(this.state.username, this.state.password);
  };

  // set the component-level state
  onChange = e => this.setState({ [e.target.name]: e.target.value });

  render() {
    console.log(this.props)
    // try login in with e.g. MamaJamaica / 123456 (or whatever user I created earlier using Postman)
    if (this.props.isAuthenticated) {
      return <Redirect to="/" />; 
      // TO DO: instead, redirect to page the user was on when going to the login page! 
      // - e.g. using useHistory from react-router-dom? - https://serverless-stack.com/chapters/redirect-on-login-and-logout.html
    }

    const { username, password } = this.state;
    return (
      <div className="content-area-centered adjust-vertical">
      {/*<div className="content-area-centered" style={{position: 'absolute', top: '40%', transform: 'translate(-50%, -50%)'}}>*/}

        <h2 className="text-center mb1">Log in</h2>

        <div className="auth-form">
          {/* <h2 className="text-center mb1">Log in</h2> */}

          <form onSubmit={this.onSubmit}>
            <div className="form-item">
              <label>Username</label>
              <input
                type="text"
                className="form-control"
                name="username"
                onChange={this.onChange}
                value={username}
                // placeholder="Username"
              />
            </div>

            <div className="form-item">
              <label>Password</label>
              <input
                type="password"
                className="form-control"
                name="password"
                onChange={this.onChange}
                value={password}
                // placeholder="Password"
              />
            </div>

            <div className="form-item" style={{background: ''}}>
              <button type="submit" className="btn-large">
                Log In
              </button>
            </div>

            {/*style={{marginTop: '1.0em'}}*/}
            {/*<p>Don't have an account? <Link to="/join">Join</Link></p>*/}
            
          </form>
        </div>

      </div>
    );
  }
}

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated // only need this part of auth so just take that, <div class="isAuthenticated
});

export default connect(mapStateToProps, { login })(Login);