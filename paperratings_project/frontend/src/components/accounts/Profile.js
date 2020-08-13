import React, { Component } from 'react';
import { connect } from 'react-redux';



export class Profile extends Component {
  render() {

    const { user } = this.props.auth; // available thx to mapStateToProps at the bottom

    return (
      <div className="content-area-full">
        <h1>Profile</h1>  
        <p>Welcome {user.username}!</p>
      </div>
    )
  }
}


const mapStateToProps = state => ({
  auth: state.auth
});

export default connect(mapStateToProps)(Profile);
