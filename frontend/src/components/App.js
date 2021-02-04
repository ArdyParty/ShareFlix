import React, { Component } from "react";
import { render } from "react-dom";
import { BrowserRouter, Route, Link, Switch } from "react-router-dom";
import Movie from './Movie/Movie';
import MovieDetail from "./MovieDetail/MovieDetail";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("api/movies")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
      <BrowserRouter>
        <div>
          <Switch>
            <Route
              exact path="/"
            >
              <ul>
                {this.state.data.map(movie => 
                  <Movie
                    key={movie.id}
                    movie={movie}
                  />
                )}
              </ul>
            </Route>
            <Route
              path="/movie/:movieId"
              // component={MovieDetail}
              render={(props) => (
                <MovieDetail
                  {...props}
                  movies={this.state.data}
                />
              )}
            >
            </Route>
          </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);