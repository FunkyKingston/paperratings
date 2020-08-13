import React, { Component, Fragment } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getPapers, deletePaper } from '../../actions/papers';
import AddPaper from '../forms/AddPaper';


export class Papers extends Component {
  static propTypes = {
    papers: PropTypes.array.isRequired,
    getPapers: PropTypes.func.isRequired,
    deletePaper: PropTypes.func.isRequired
  };

  // general execution order: constructor(), componentWillMount() (deprecated), render(), componentDidMount(), <div class=""></div>
  // - Papers.js: render() called -> componentDidMount() called -> after redux state & thus mapped props updated, render() called again
  componentDidMount() {
    this.props.getPapers(); 
    // - TO DO: add a check to see if desired data is already in redux state? then no need to get again
    // console.log("ran componentDidMount() in Papers.js ...") 
    // console.log(this.props);
    // console.log("----------")
  }

  componentDidCatch(error, info) {
    console.log("ran componentDidCatch in Papers.js ...")
    this.setState({error, info}) // ?
  }

  render() {
    // console.log("this.props in render():");
    // console.log(this.props);
    // console.log("----------")

    return (
      <div className="content-area-split">
        <div className="main-content">

          {/* <AddPaper /> */}

          <p>page 1 of X</p>
          {/* - TO DO: Add pagination https://www.django-rest-framework.org/api-guide/pagination/ */}
          <hr />
          
          { 
            this.props.papers.map(paper => (
              <div key={paper.id} className="paper-item">
                <h3><Link className="link-style" to ={`/paper/${paper.id}`}>{paper.title}</Link></h3>
                <p className="mb1">by {paper.authors}</p>
                <p className="mb1">{paper.rating} avg rating - ({paper.num_ratings}) - published {paper.date_published}</p>
                <button onClick={this.props.deletePaper.bind(this, paper.id)} className="btn-small-transparent">Delete</button>
              </div>
            )) // about needing to use .bind() with functions - https://reactjs.org/docs/handling-events.html
               // - using this.props.deletePaper without bind (.bind(this, paper.id)) -> Error: "DELETE http://127.0.0.1:8000/api/papers/[object%20Object]/ 404 (Not Found)"
               // btw, don't use "this.props.deletePaper() - the () makes the function run, thus deleting all papers!
               
          }

          <br />
          <AddPaper />

        </div>

        <div className="side-content">
          <div className="side-image">
            <img src="../../../static/img/capybara.png" width="190"/>
          </div>

          {/* <div className="paper-filters" style={{"background": "red"}}>abc</div> */}
          <div className="paper-filters sans-serif">
            <div><p><b>Filter search results:</b></p></div>
            <div><p>Categories</p></div>
          </div>
          
        </div>

      </div> 
    );
  }
}



// map the state of redux to [this.props.]papers
// - state.papers means that we want the state of the papers reducer, whose state is also named papers, thus the final .papers
const mapStateToProps = state => ({
  papers: state.papers.papers
});

export default connect(
  mapStateToProps, 
  { getPapers, deletePaper }
)(Papers);
