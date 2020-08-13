import React, { Component } from 'react'

export class About extends Component {
  // componentDidMount() {
  //   console.log("ran componentDidMount in About.js ...") 
  //   console.log(this.props);
  //   console.log("----------")
  // }
  
  render() {
    // console.log(`ran render() in About.js ...`);

    return (
      <div className="content-area-split">
        <div className="main-content">
        
          <h1>About</h1>
          <div className="about-item">
            <p className="mb1">This webpage is built with Django and React, and is one of my personal "projects" on my recent mission to learn more in the field of web development. So who am I? I am an Electrical Engineer and a PhD in digital image processing, an interest in machine learning and of course in IT development! Some of my other hobbies social dancing (mainly Kizomba) and DJing!</p>
            <p className="mb1">My LinkedIn profile is found <a href="https://www.linkedin.com/in/tomas-bengtsson-17bba412/" target="_blank" style={{"color": "black"}}>here</a>.</p>
            <p className="mb1">The code for this site is available at Github in this repository - upload and add link!</p>
          </div>

          <hr />
          <div className="about-item">
            <h3 id="howtouse">How to use</h3>
            <p className="mb1">The intention with this (as of now incomplete) website is to provide a searchable database of scientific papers (read from and continuously updated from external APIs), as well as functionality to comment/leave reviews, rate papers, and to save and organize favorite papers as a logged in user.</p>
            <p className="mb1">Currently, there is a papers API which is accessible to all users (no login required) to provide a temporary list of papers to test other functionality with. It is possible to create an account, to log in, to view a paper details page, and to add/edit/delete comments for papers. The API is setup using Django and the data is currently stored in a relational database.</p>
          </div>

          <hr />
          <div className="about-item">
            <h3 id="openapi">Open API</h3>
            <p className="mb1">Some of the current API endpoints are listed here (tentative list):</p>
            <div style={{"width": "100%"}}>
              <ul style={{"listStylePosition": "inside", "marginBottom": "0.6rem"}}> {/* https://www.w3schools.com/cssref/pr_list-style-position.asp */}
                <li>/api/papers/</li>
                <li>/api/papers/1/</li>
                <li>/api/comments/</li>
                <li>/api/comments/1/</li>
                <li>/api/commentdetails/</li>
                <li>/api/commentdetails/1/</li>
                <li>/api/commentlistbypaper?paper_id=1</li>
                <li>/api/auth/profile/1/ - <i>currently no special permissions needed (a "User" has a "Profile")</i></li>
                <li>/api/auth/user - <i>requires the user's unique token to be specified in the request header. endpoint not part of the "open API"</i></li>
              </ul>
            </div>
          </div>

          <hr />
          <div id="community" className="about-item">
            <h3>Community</h3>
            <p className="mb1">Perhaps the website will also include some sort of community section, with events such as local PhD pubs etc.! </p> 
          </div>


        </div>

        <div className="side-content">
          <div className="side-image">
            <img src="../../../static/img/capybara.png" width="190" style={{marginLeft: 0, marginRight: 0}} />
          </div>


          <div>
            <ul className="about-headers sans-serif">
              <li><a href="#howtouse" className="link-style">How to use</a></li>
              <li><a href="#openapi" className="link-style">Open API</a></li>
              <li><a href="#community" className="link-style">Community</a></li>
            </ul>
          </div>
        </div>


      </div>
    )
  }
}

export default About;
