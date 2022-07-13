import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getOneGameInfo } from '../src/store/game';
import Home from '../src/components/Home';
import Game from '../src/components/Game';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();
  const game = useSelector(state => state.game);

  useEffect(() => (async() => await dispatch(getOneGameInfo()).then(() => setLoaded(true)))(), [dispatch]);
  
  if (!loaded) {
    return null;
  }
  
  return (
    <div>{ game.game_started ? <Game game={game} /> : <Home game={game} /> }</div>
  );
}

export default App;
