import React from 'react';

const MovieDetail= ({match, movies}) => {
  const movie = movies.find((m) => m.id === parseInt(match.params.movieId));
  return (
    <div>
      <h1>{match.params.movieId}</h1>
      <h1>{movie["title"]}</h1>
    </div>
  )
}

export default MovieDetail;