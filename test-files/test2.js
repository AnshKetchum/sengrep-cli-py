import React, { useState } from 'react';
const Form = () => {
    const [name, setName] = useState('');
    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(`Form submitted, ${name}`);    
    }
    return(
        <>
            <input onChange = {(e) => setName(e.target.value)} value = {name}></input>
            <button type = 'submit'>Click to submit</button>
        </>
    );
}
export default Form;