import React, { Component } from 'react';
import { connect } from 'react-redux';

/* 
  TO DO: (Also for MyPapers.js) 
  - going to http://127.0.0.1:8000/profile in the browser address bar redirects to the home view '/', but works for e.g. '/about'
    - seems to be some error with the links that require login to access, even when being logged in
*/

export class Profile extends Component {
  // componentDidMount() {
  //   console.log(`this.props.auth:`)
  //   console.log(this.props.auth)
  // }

  render() {

    // console.log(`this.props.auth:`)
    // console.log(this.props.auth)

    const { user } = this.props.auth; // available thx to mapStateToProps at the bottom
    console.log(user)

    return (
      <div className="content-area-full">
        <h1>Profile</h1>  
        <p>Welcome {user.username}!</p>
        {/* <p><img src={user.profile.image} style={{"borderRadius": "50%", "marginTop": "1rem", "height": "6rem", "width": "6rem"}}/></p> */}
        {/* <p>{user.profile.image}</p> */}
      </div>
    )
  }
}


const mapStateToProps = state => ({
  auth: state.auth
});

export default connect(mapStateToProps)(Profile);
