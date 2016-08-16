def make_container(file_name, component_path):
    container = open('containers/' + file_name + '.js', 'w')
    container.write("""
    import { connect } from 'react-redux';
    import""" + file_name + """ from '""" + component_path + """';
    import {BlankFunction} from '../actions/""" + file_name + """';
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
    )(""" + file_name + """);
    """)
    container.close()