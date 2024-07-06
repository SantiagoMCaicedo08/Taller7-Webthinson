import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './TipodocumentoList.css';

const TipodocumentoList = () => {
    const [tipodocumentos, setTipodocumentos] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/tipodocumento/')
            .then(response => {
                setTipodocumentos(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the tipodocumentos!', error);
            });
    }, []);

    return (
        <div className="tipodocumento-list">
            <h1>Lista de Tipos de Documento</h1>
            <ul>
                {tipodocumentos.map(tipodocumento => (
                    <li key={tipodocumento.id} className="tipodocumento-item">
                        <span className="tipodocumento-title">{tipodocumento.nombre}</span>: <span className="tipodocumento-description">{tipodocumento.descripcion}</span>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TipodocumentoList;