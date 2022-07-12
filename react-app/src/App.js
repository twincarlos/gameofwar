import React, { useState, useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { getOneGameInfo } from '../src/store/game';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(getOneGameInfo()).then(() => setLoaded(true));
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <div>
      
    </div>
  );
}

export default App;
