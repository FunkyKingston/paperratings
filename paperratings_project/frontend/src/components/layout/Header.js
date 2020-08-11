import React, { Component, Fragment } from 'react';
import { Link } from 'react-router-dom';
//import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { logout } from '../../actions/auth';


/*
  TO DO: After login, redirect to previous page instead of 
  - https://www.google.com/search?q=usehistory+redirect+from+login+page+to+previous+page&oq=usehistory+redirect+from+login+page+to+previou&aqs=chrome.1.69i57j33l3.11151j0j7&sourceid=chrome&ie=UTF-8
    - "Redirect on Login and Logout": https://serverless-stack.com/chapters/redirect-on-login-and-logout.html
  - https://reactrouter.com/web/api/Hooks
*/


function Burger(props) {
  return (
    <div className={props.classList} onClick={props.onToggleDropdown}> 
      <div className="line1"></div>
      <div className="line2"></div>
      <div className="line3"></div>
    </div>
  )
}


export class Header extends Component {
  state = {
    dropdownOpen: false
  };

  static propTypes = {
    auth: PropTypes.object.isRequired,
    logout: PropTypes.func.isRequired
  };

  onToggleDropdown = () => {
    this.setState((prevState) => {
      return {dropdownOpen: !prevState.dropdownOpen};
    });
  };

  closeDropdown = () => this.setState({dropdownOpen: false});

  onLogoutLink = () => {
    this.closeDropdown();
    this.props.logout();
  };

  render() {
    const { isAuthenticated, user } = this.props.auth; // available thx to mapStateToProps at the bottom
    
    const authLinks = (
      <ul>
        <li><Link to={'/mypapers'} onClick={this.closeDropdown}>My Papers</Link></li>
        <li><Link to={'/profile'} onClick={this.closeDropdown}>Profile</Link></li>
        {/* <li><Link to={'/'} onClick={this.props.logout}>Log Out</Link></li> */}
        <li><Link to={'/'} onClick={this.onLogoutLink}>Log Out</Link></li>
      </ul>
    );

    const guestLinks = (
      <ul>
        <li><Link to={'/login'} onClick={this.closeDropdown}>Log In</Link></li>
        <li><Link to={'/join'} onClick={this.closeDropdown}>Join</Link></li>
      </ul>
    );

    let rightLinks;
    if (isAuthenticated) {
      rightLinks = authLinks;
    } else {
      rightLinks = guestLinks;
    }

    // let burgerElement = document.getElementsByClassName("burger");
    // burgerElement.classList.add("open");
    // console.log(burgerElement);
    // let tmp = document.getElementById("tmp")
    // let tmp = document.getElementById("tmp").classList.add("mynewclass");
    // tmp.classList.add("test");
    // console.log(tmp);
    

    return (
      <Fragment>
          
        <nav>

          <div className="dummy-burger"></div> {/* to achieve centering of logo in low screen width media query - another option could be to use a grid box approach */ }

          <div className="nav-flex-item nav-links">
            <ul>
              {/* The onClick function is not needed here (just sets dropdownOpen, already false, to false again) as there is no dropdown navbar in full width mode, however until refactoring code, keep all <Link> similar */}
              <li><Link to={'/'} onClick={this.closeDropdown}>Home</Link></li>
              <li><Link to={'/about'} onClick={this.closeDropdown}>About</Link></li>
            </ul>
          </div>

          <div className="nav-flex-item nav-logo">
            <h3><Link className="no-text-decoration" to={'/'}>PaperRatings.com</Link></h3>
          </div>

          <div className="nav-flex-item nav-links">
            { isAuthenticated ? authLinks : guestLinks }
          </div>
          
          {this.state.dropdownOpen ?
            <Burger classList={"burger burger-open"} onToggleDropdown={this.onToggleDropdown} />
            :
            <Burger classList={"burger"} onToggleDropdown={this.onToggleDropdown} />
          }
        </nav>

        
        {this.state.dropdownOpen ?
          <div className="nav-links-dropdown" >
            <ul>
              <li><Link to={'/'} onClick={this.closeDropdown}>Home</Link></li>
              <li><Link to={'/about'} onClick={this.closeDropdown}>About</Link></li>
            </ul>
            { isAuthenticated ? authLinks : guestLinks }
          </div>
          :
          ""
        }

      </Fragment>
  
    )
    
  }
}

const mapStateToProps = state => ({
  auth: state.auth
});

export default connect(mapStateToProps, { logout })(Header);

//export default withRouter(Header);
