
    import { connect } from 'react-redux';
    importComponentName from 'actions/ComponentName.js';
    import {BlankFunction} from '../actions/ComponentName';
    const mapStateToProps = (state) => {
      return {
        SomeBool: true
      };
    };

    const mapDispatchToProps = (dispatch, ownProps) => {
      return {
        acceptCurrent: () => {
          dispatch(BlankFunction());
        }
      };
    };

    export default connect(
      mapStateToProps,
      mapDispatchToProps
    )(ComponentName);
    