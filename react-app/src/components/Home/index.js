import "../Home/Home.css";
import { useDispatch } from 'react-redux';
import { getOneGameInfo, startOneGame } from '../../store/game';

function Home() {
    const dispatch = useDispatch();

    return (
        <div id="home-main">
            <h1>Welcome to Game of War</h1>
            <button onClick={async () => await dispatch(startOneGame()).then(() => dispatch(getOneGameInfo()))}>Press to Start</button>
        </div>
    );
}

export default Home;