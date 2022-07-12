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

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_GAME_INFO:
            state = action.gameInfo;
            return state;
        default:
            return state;
    }
}