import './App.css';
import React, {useState, useEffect} from 'react';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import RecommendedTournament from './pages/RecommendedTournament';
import RecommendedTournamentById from './pages/RecommendedTournamentById';
import JoinTournament from './pages/JoinTournament';
import Home from './pages/Home';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element= {<Home/>}/>
        <Route path="/recommended_tournament" element= {<RecommendedTournament/>}/>
        <Route path="/recommended_tournament/:user_id" element= {<RecommendedTournamentById/>}/>
        <Route path="/join_tournament/:team_id/:tournament_id" element= {<JoinTournament/>}/>
      </Routes>
    </Router>
  );
}

export default App;
