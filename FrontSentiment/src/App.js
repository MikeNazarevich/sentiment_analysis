import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Main from'./Main';


class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Sentiment analysis</h1>
        </header>

        <Main/>
        <div id="footer">created by Mikhail Nazarevich</div>
      </div>
      
    );
  }
}

export default App;
