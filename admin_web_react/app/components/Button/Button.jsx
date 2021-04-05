import React, { Component } from 'react'

import styles from './style.css'

export default class Button extends Component {
    render() {
        let bgColor = {backgroundColor : this.props.bgColor}
        return (
            <button className={styles.button} onClick={this.props.onClick} style={bgColor}>{this.props.value.toUpperCase()}</button>
        )
    }
}
