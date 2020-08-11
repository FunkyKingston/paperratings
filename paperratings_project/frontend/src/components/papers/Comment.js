import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { editComment, deleteComment } from '../../actions/comments';


export class Comment extends Component {
  // "Where to Initialize State in React" - https://daveceddia.com/where-initialize-state-react/
  state = { 
    isEditing: false,
    newCommentText: this.props.comment.text
  };

  static propTypes = {
    editComment: PropTypes.func.isRequired,
    deleteComment: PropTypes.func.isRequired
  };

  // https://reactjs.org/docs/state-and-lifecycle.html - read up on pitfalls when using setState(): https://reactjs.org/docs/faq-state.html
  doEdit = e => this.setState({ isEditing: true });
  // below variant better? is there any difference for the current scenario?
  // doEdit = e => this.setState((state) => { // important, state - not this.state, with this function
  //   return {isEditing: true}
  // });

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {
    e.preventDefault();
    // console.log('submit edit comment... this.props.comment:');
    // console.log(this.props.comment)

    const { id, text, time, user_data } = this.props.comment;

    // comment data that will be sent to the django backend, following the format of CommentSerializer (not CommentDetailSerializer)
    // - the redux state for comments however follows the format of CommentDetailSerializer - handled by actions/comments.js, reducers/comments.js
    const newComment = {
      id: id,
      text: this.state.newCommentText,
      time: time,
      profile: user_data.id,
      paper: this.props.currentPaper.id
    };
  
    this.props.editComment(newComment);
    this.setState({ isEditing: false });
  };

  
  render() {
    const { comment, auth } = this.props;
    // console.log("render(), comment and auth objects:")
    // console.log(comment)
    // console.log(auth)

    let byLoggedInUser = false;
    if (this.props.auth.isAuthenticated) {
      if (this.props.auth.user.id == this.props.comment.user_data.id) {  // using CommentDetailsSerializer (see papers/serializers.py)
        byLoggedInUser = true;
      }
    }

    // https://programmingwithmosh.com/javascript/react-lifecycle-methods/
    return (
      <div key={comment.id}>
        {/* If-else-in-JSX: https://react-cn.github.io/react/tips/if-else-in-JSX.html */}
        {!this.state.isEditing ? 
          
          <div className="comment-item">
            <h4>By {comment.user_data.username}</h4>
            <p className="mb1">{comment.text}</p>  
            {
              byLoggedInUser && // https://reactjs.org/docs/conditional-rendering.html
                <div>
                  {/* 
                    About using setState() in the render() function (which should be kept pure) - https://reactjs.org/docs/react-component.html   
                    - https://blog.logrocket.com/an-imperative-guide-to-setstate-in-react-b837ceaf8304/
                    - *** https://stackoverflow.com/questions/51497506/calling-setstate-in-an-eventhandler-in-the-render-method
                      - "It is fine to have event handlers that update the state in the render method, as long as they are only called when that event is fired."
                    - https://stackoverflow.com/questions/38332068/setting-state-with-onclick-in-render-function/38332217
                    - 
                  */}
                  <button onClick={this.doEdit} className="btn-small-transparent">Edit</button> 
                  <button onClick={this.props.deleteComment.bind(this, comment.id)} className="btn-small-transparent">Delete</button>
                </div>
            }
          </div>

          :

          <div className="comment-item">
            <h4>By {comment.user_data.username}</h4>
            <form onSubmit={this.onSubmit}>
              <div className="form-item">
                <textarea
                  className="form-control"
                  type="text"
                  name="newCommentText"
                  onChange={this.onChange}
                  value={this.state.newCommentText}
                />
              </div>
              <button type="submit" className="btn-small-transparent">Submit</button>
            </form>
          </div>

        }
      </div>
    )
  }
}

// connect() vs React Component lifecycle methods, connect() lifecycle comes before the Component lifecycle:
// - https://stackoverflow.com/questions/50735735/order-of-component-life-cycle-with-react-redux-connect-and-redux-data
export default connect(
  // mapStateToProps, 
  null,
  { editComment, deleteComment }
)(Comment);

