import React from 'react';
import './App.css';
import TipodocumentoList from './components/TipodocumentoList';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>Bienvenido a la Aplicación</h1>
            </header>
            <TipodocumentoList />
        </div>
    );
}

export default App