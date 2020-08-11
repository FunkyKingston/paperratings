import React, { Component, Fragment } from 'react';

import { Link } from 'react-router-dom';

import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getComments, deleteComment } from '../../actions/comments';
import { getPaper } from '../../actions/papers';

import Comment from './Comment';
import AddComment from '../forms/AddComment';


/*
TO DO: Add "rate paper" functionality, check out some useful packages, maybe this? https://www.npmjs.com/package/react-star-ratings

TO DO: Avoid loading page before data is fetched from backend:
- https://stackoverflow.com/questions/57203298/react-js-how-to-prevent-rendering-before-state-being-updated-hooks
  - 1. Have the component render itself in a "loading" state
  OR
  - 2. Don't create the component until you have the data — e.g., move the fetch operation into its parent, ...
*/

export class PaperDetails extends Component {
  // state = { 
  //   isLoaded: false
  // };
  
  static propTypes = {
    currentPaper: PropTypes.object.isRequired,
    comments: PropTypes.array.isRequired,
    getPaper: PropTypes.func.isRequired,
    getComments: PropTypes.func.isRequired
  };
  
  /*
  About React component, lifecycle methods, setState() etc.
  - https://reactjs.org/docs/react-component.html
  - https://reactjs.org/docs/state-and-lifecycle.html
  - https://reactjs.org/docs/faq-state.html
  - https://css-tricks.com/understanding-react-setstate/
  */

  componentDidMount() {
    // this.props.getPaper(this.props.match.params.id)
    // this.props.getComments(this.props.match.params.id)

    console.log(`ran componentDidMount() in PaperDetails.js ... with this.props.match.params.id = ${this.props.match.params.id}`);
    console.log(this.props); // "match" prop added by BrowserRouter - as demonstrated in https://www.youtube.com/watch?v=Law7wfdg_ls
    console.log("----------")    


    if(this.props.currentPaper.id) {
      console.log("this.props.currentPaper.id is defined");
      console.log(`this.props.currentPaper.id = ${this.props.currentPaper.id}`);
      console.log(`this.props.match.params.id = ${this.props.match.params.id}`);
      if(this.props.match.params.id != this.props.currentPaper.id) {
        this.props.getPaper(this.props.match.params.id)
        this.props.getComments(this.props.match.params.id)
      };
    } else {
      console.log("this.props.currentPaper.id is NOT defined");
      this.props.getPaper(this.props.match.params.id)
      this.props.getComments(this.props.match.params.id)
    };
  }

  // https://lucybain.com/blog/2017/react-js-when-to-rerender/ - "Writing and running computations in shouldComponentUpdate can be expensive so you should to make sure they’re worth the time. Before writing any shouldComponentUpdates you can check how many wasted cycles React does by default."
  // - "render() will not be invoked if shouldComponentUpdate() returns false." (by default it returns true, can override) - https://reactjs.org/docs/react-component.html 
  // shouldComponentUpdate(nextProps) { 
  //   console.log(`ran ShouldComponentUpdate() in PaperDetails.js ... with this.props.match.params.id = ${this.props.match.params.id}`);
  //   console.log(this.props);
  //   console.log(nextProps);
  //   return true; // must return true or false, just keeping as the default true here for now
  // }

  // // componentDidUpdate(prevProps, prevState, snapshot) {
  // componentDidUpdate(prevProps) {  
  //   console.log(`ran componentDidUpdate() in PaperDetails.js ... with this.props.match.params.id = ${this.props.match.params.id}`);
  //   // console.log(prevProps, prevState, snapshot);
  //   console.log(prevProps);
  //   console.log(this.props);
  // }

  render() {
    console.log(`ran render() in PaperDetails.js ... with this.props.match.params.id = ${this.props.match.params.id}`) 
    const { currentPaper, auth } = this.props;

    //const { id } = this.props.match.params;
    //console.log(`render paper details for paper with id: ${id}`)
    // console.log("Print this.props from PaperDetails render function")
    // console.log(this.props);
    
    // console.log(`this.state.isLoaded: ${this.state.isLoaded}`);

    return (
      <div className="content-area-full">
        {/* <p>TMP: primary key of current paper: {this.props.match.params.id}</p> */}
        
        {/* {this.state.isLoaded ?  */}
        {this.props.match.params.id == this.props.currentPaper.id ? // as else-statement e.g. a spinner can be displayed
          <div>
          <div className="paper-details">
            <h3>{currentPaper.title}</h3>
            <p className="mb1">by {currentPaper.authors}</p>
            <p className="mb1">published {currentPaper.date_published} {currentPaper.journal ? `in ${currentPaper.journal}` : ''}</p>
            <p className="mb1">{currentPaper.rating} avg rating - ({currentPaper.num_ratings})</p>
            <hr />
            <p className="mb1"><b>Abstract</b> {currentPaper.abstract}</p>
          </div>
          
          <br />
          {/* <h3 className="sans-serif">REVIEWS</h3> */}
          <h3 className="sans-serif">COMMENTS</h3>
          <hr />

          {
            (this.props.comments === undefined || this.props.comments.length == 0) ?
              // - https://stackoverflow.com/questions/24403732/how-to-check-if-array-is-empty-or-does-not-exist
              <p className="mb1">Add the first comment for this paper!</p>
              // console.log("there are no comments for this paper")
              :
              console.log("there are comments for this paper!")
          }

          { 
            this.props.comments.map(comment => (
              <Comment key={comment.id} currentPaper={currentPaper} auth={auth} comment={comment} />
            ))
          }
          
          { 
            this.props.auth.isAuthenticated ? 
              <AddComment />
              :
              <p className="mb1">Please log in <Link to={'/login'} style={{color:" black"}}>log in</Link> to add a comment!</p>
              // TO DO: add redirect based on page history, to go back to the same PaperDetails-page after logging in 
              // - e.g. using useHistory from react-router-dom? - https://serverless-stack.com/chapters/redirect-on-login-and-logout.html
          }
          </div>

          :
          ""
          // <div>
          //   <p>this.state.isLoaded is False!</p>
          // </div>
        }

      </div>
    )
  }
}

const mapStateToProps = state => ({
  auth: state.auth,
  currentPaper: state.papers.currentPaper,
  comments: state.comments.comments
});

export default connect(
  mapStateToProps, 
  { getPaper, getComments }
)(PaperDetails);






