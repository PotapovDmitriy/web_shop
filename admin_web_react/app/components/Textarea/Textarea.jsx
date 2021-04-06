import React, { Component } from 'react'
import classnames from 'classnames'

import styles from './style.css'

export default class Textarea extends Component {
    render() {
        return (
            <div className={styles.textareaBlock}>
                <label htmlFor={this.props.id} className={classnames(styles.label, this.props.className)}>{this.props.label}</label>
                <textarea className={classnames(styles.textarea, this.props.className)}
                    placeholder={this.props.placeholder}
                    onChange={(e)=>{this.props.onChange(e)}}
                    id={this.props.id}
                    value={this.props.value}/>
            </div>
            
        )
    }
}
