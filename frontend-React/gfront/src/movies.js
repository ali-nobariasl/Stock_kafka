
import React from 'react';
import { gql, useQuery } from '@apollo/client';









const GET_MOVIES = gql`
{
    allMovies{
        edges{
            node{
                id
                title
                year
            }
        }
    }
}`








function Movies(){

    const { loading, error, data}= useQuery(GET_MOVIES);
    if (loading) return 'Loading...';
    if (error) return 'Error.${error.message}';

    const movies = data.allMovies.edges;

    return(
        <div>
            <h1>List of movies</h1>
            {
                movies.map(movie =>{
                    return <h2 key={movie.node.id}> {movie.node.title} </h2>
                })
            }
        </div>
    )
}

export default Movies;