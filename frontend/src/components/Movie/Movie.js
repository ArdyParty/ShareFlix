import React from 'react';
import { Link } from "react-router-dom";

const Movie = ({movie}) => {
  return (
    <div>
      <li>
        <Link to={`/movie/${movie.id}`}>
          { movie.title} - {movie.profile} - {movie.how_heard}
        </Link>
      </li>
    </div>
  )
}

export default Movie;