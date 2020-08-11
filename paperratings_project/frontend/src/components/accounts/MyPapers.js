import React, { Component } from 'react';
import { connect } from 'react-redux';


export class MyPapers extends Component {
  render() {
    return (
      <div className="content-area-full">
        <h1>My papers</h1>
      </div>
    )
  }
};


const mapStateToProps = state => ({
  auth: state.auth // may not use in this component, let's see
});

export default connect(mapStateToProps)(MyPapers);