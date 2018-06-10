import React, { Component } from 'react';


class Main extends Component {
    constructor(props) {
        super(props);
        this.state = {
            value: '',
            tonality: '',
            stl: '',
            margTop: '100px'
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        event.preventDefault();
        this.handleRequest(this.state.value)
    }

    async handleRequest(value) {
        await fetch('http://127.0.0.1:5000/get_record', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'},
            body: JSON.stringify({
                'record': value
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)

            if (data === 'positive') {
                this.setState({tonality: 'positive'})
                this.setState({stl: 'posAnswer'})
            }
            else {
                this.setState({tonality: 'negative'})
                this.setState({stl: 'negAnswer'})
            }
            this.setState({margTop: '45px'})
            
        })
        .catch(error => console.log(error))
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit} className="Main">
                <div className={this.state.stl}> {this.state.tonality.toUpperCase()} </div>
                <textarea className="area" style={{marginTop: this.state.margTop}} placeholder="Введите текст..." type="text" value={this.state.value} onChange={this.handleChange} cols="60" rows="5"></textarea>
                <input className="butt" type="submit" value="Определить"/>
            </form>
        )
    }
}

export default Main;