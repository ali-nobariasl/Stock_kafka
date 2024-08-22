import logo from './logo.svg';
import './App.css';
import Movies from './movies';

import { ApolloClient, InMemoryCache, ApolloProvider } from '@apollo/client'; 




const client = new ApolloClient({
  uri : "http://127.0.0.1:8000/graphql/",
  cache: new InMemoryCache()  
});


function App() {
  
  return (
    <ApolloProvider client={client}>
      <div className="App">
        <Movies />
      </div>
    </ApolloProvider>
  );
}

export default App;
