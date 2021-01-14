import React from 'react';

const Movie = ({key, movie}) => {
  return (
    <div>
      <li key={movie.id}>
        {movie.title} - {movie.profile} - {movie.how_heard}
      </li>
    </div>
  )
}

export default Movie;