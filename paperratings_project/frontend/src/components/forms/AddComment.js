import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addComment } from '../../actions/comments';


export class AddComment extends Component {
  state = { // component-level state (as opposed to redux state)
    commentText: ""
  };

  // propTypes - "not necessary, just good practice" - https://www.npmjs.com/package/prop-types
  static propTypes = {
    addComment: PropTypes.func.isRequired
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {
    e.preventDefault();

    if(this.props.auth.isAuthenticated) {
      const comment = {
        text: this.state.commentText,
        // time: // set by backend to current time
        profile: this.props.auth.user.id, 
        paper: this.props.currentPaper.id
      };
      this.props.addComment(comment);
      this.setState({ commentText: "" });
    };
  };

  render() {
    
    const { commentText } = this.state; // component-level state

    
    /* 
      TO DO: No need to use redux/mapStateToProps here, the used redux state elements are available in 
      the parent component PaperDetails.js - consider passing them down as props directly from there 
    */

    return (
      <Fragment>
        
        <h3 className="sans-serif">ADD COMMENT</h3>

        <div>
          <form onSubmit={this.onSubmit}>
            <div className="form-item">
              {/* <label>Comment</label> */}
              <textarea
                className="form-control"
                type="text"
                name="commentText"
                onChange={this.onChange}
                value={commentText}
              />
            </div>
            <button type="submit" className="btn-small-blue">Submit</button>
          </form>
        </div>
      </Fragment>
    )
  }
}

const mapStateToProps = state => ({ // better to replace this and just pass props down from PaperDetails? only parent for AddComments.js
  auth: state.auth,
  currentPaper: state.papers.currentPaper
});


export default connect(mapStateToProps, { addComment })(AddComment);
