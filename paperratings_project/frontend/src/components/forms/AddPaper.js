import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addPaper } from '../../actions/papers';


export class AddPaper extends Component {
  state = {
    title: "",
    authors: "",
    abstract: "",
    journal: "",
    date_published: "",
    doi: "",
    pdflink: ""
  };

  // propTypes - "not necessary, just good practice" - https://www.npmjs.com/package/prop-types
  static propTypes = {
    addPaper: PropTypes.func.isRequired
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {
    e.preventDefault();
    console.log('submit');
    const { title, authors, abstract, journal, date_published, doi, pdflink } = this.state;
    const paper = {
      title: title,
      authors: authors,
      abstract: abstract,
      journal: journal,
      date_published: date_published,
      doi: doi,
      pdflink: pdflink
    };

    this.props.addPaper(paper);
    // Compare to Papers.js:   this.props.deletePaper.bind(this, paper.id)   <- when to use/not to use .bind() ?
    // - ...
  };

  // bootstrap classes, see at https://bootswatch.com/4/cosmo/bootstrap.css
  render() {
    const { title, authors, abstract, journal, date_published, doi, pdflink } = this.state;
    return (
      <Fragment>

        <h3 className="sans-serif">ADD PAPER (Manual entry for now, to implement and test other functionality)</h3>
        <p className="mb1">...you can also interact with the papers API at /api/papers/ (the trailing backslash is necessary)</p>
        
        <div>

          <form onSubmit={this.onSubmit}>
            <div className="form-item">
              <label>Title</label>
              <input
                className="form-control"
                type="text"
                name="title"
                onChange={this.onChange}
                value={title}
              />
            </div>
            <div className="form-item">
              <label>Authors</label>
              <input
                className="form-control"
                type="text"
                name="authors"
                onChange={this.onChange}
                value={authors}
              />
            </div>
            <div>
              <label>Journal</label>
              <input
                className="form-control"
                type="text"
                name="journal"
                onChange={this.onChange}
                value={journal}
              />
            </div>
            <div>
              <label>Publication date</label>
              <input
                className="form-control"
                type="date"
                name="date_published"
                onChange={this.onChange}
                value={date_published}
              />
            </div>
            <div className="form-item">
              <label>Abstract</label>
              <textarea
                className="form-control"
                type="text"
                name="abstract"
                onChange={this.onChange}
                value={abstract}
              />
            </div>
            <button type="submit" className="btn-small-blue">Submit</button>
          </form>
          
        </div>
      </Fragment>
    );
  }
}

export default connect(null, { addPaper })(AddPaper);