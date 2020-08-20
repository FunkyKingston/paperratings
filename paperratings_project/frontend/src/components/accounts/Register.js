import React, { Component } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { register } from '../../actions/auth';
// import { createMessage } from '../../actions/messages'; // not done, pt4/7 of the vid series https://www.youtube.com/watch?v=kfpY5BsIoFg&list=PLillGF-RfqbbRA-CIUxlxkUpbq0IFkX60&index=7


export class Register extends Component {
  // component-level state, has nothing to do with redux
  state = {
    username: '',
    email: '',
    password: '',
    password2: '',
  };

  static propTypes = {
    register: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool
  }

  onSubmit = e => {
    e.preventDefault();
    // console.log('register submit')
    const { username, email, password, password2 } = this.state;
    if(password !== password2 ) {
      // not implemented (yet) - this.props.createMessage({ passwordsNotMatch: 'Passwords do not match'})
      // console.log('register submit, passwords do not match')
    } else {
      // console.log('register submit, passwords DO match')
      const newUser = {
        username,
        password,
        email
      }; // a new user object
      this.props.register(newUser); 
      // calls the (imported) register function in the auth.js reducer
    }
  };

  // set the component-level state
  onChange = e => this.setState({ [e.target.name]: e.target.value });

  render() {
    // try login in with e.g. MamaJamaica / 123456 (or whatever user I created earlier using Postman)
    if (this.props.isAuthenticated) {
      return <Redirect to="/" />;
    }

    const { username, email, password, password2 } = this.state;
    return (
      <div className="content-area-centered adjust-vertical">

        <h2 className="text-center mb1">Create account</h2>

        <div className="auth-form">
          
          <form onSubmit={this.onSubmit}>
            {/* <div className="form-item" style={{background: 'green'}}> */}
            <div className="form-item">
              <label>Username</label>
              <input
                type="text"
                className="form-control"
                name="username"
                onChange={this.onChange}
                value={username}
              />
            </div>

            <div className="form-item">
              <label>Email</label>
              <input
                type="email"
                className="form-control"
                name="email"
                onChange={this.onChange}
                value={email}
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
              />
            </div>

            <div className="form-item" style={{background: ''}}>
              <label>Confirm password</label>
              <input
                type="password"
                className="form-control"
                name="password2"
                onChange={this.onChange}
                value={password2}
              />
            </div>

            <div className="form-item" style={{background: ''}}>
              <button type="submit" className="btn-large">
                Join
              </button>
            </div>
            

            <p style={{fontSize: '0.9rem', marginTop: '1.2rem', color: '#ccc'}}>Already have an account? <Link to="/login" style={{color: "#ccc"}}>Log in</Link></p>

          </form>

        </div>
      </div>
    );
  }
}



//export default Register;


const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated // only need this part of auth so just take that, <div class="isAuthenticated
});

export default connect(mapStateToProps, { register })(Register);