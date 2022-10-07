import axios from 'axios';
import { useState, useEffect } from 'react';

const Homepage = () => {
    const [test, setTest] = useState('')

    useEffect(() => {
        const fetchData = async () => {
            const t = await axios.get('/test')
            setTest(t.data)
        }
        fetchData()
    }, [])


    return <>
        <h1>Homepage</h1>
        <h3>{test}</h3>
    </>
}

export default Homepage