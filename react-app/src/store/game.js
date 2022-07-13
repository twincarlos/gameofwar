const initialState = {};

const GET_GAME_INFO = 'game/GAME_INFO';
const getGameInfo = gameInfo => ({
    type: GET_GAME_INFO,
    gameInfo
});
export const getOneGameInfo = () => async dispatch => {
    const response = await fetch('/api/game');
    const gameInfo = await response.json();
    dispatch(getGameInfo(gameInfo));
}

const START_GAME = 'game/START_GAME';
const startGame = () => ({
    type: START_GAME
});
export const startOneGame = () => async dispatch => {
    await fetch('/api/game/start', { method: 'PUT' })
    .then(() => dispatch(startGame()));
}

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_GAME_INFO:
            state = action.gameInfo;
            return state;
        case START_GAME:
            return state;
        default:
            return state;
    }
}