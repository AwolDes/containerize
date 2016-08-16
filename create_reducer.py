def make_reducer(file_name):
    reducer = open('reducers/' + file_name + '.js', 'w')
    reducer.write("""
    const initialState = Object.assign({}, {
      SomeBool: false
    }
    export default function""" + file_name + """"(state = initialState, action) {
      switch (action.type) {
        case 'SOME_STRING':
          const ChangeState = {
                SomeBool: true
            }
          });
          return Object.assign({}, state, ChangeState);
        default:
          return state;
      }
    }
    """)
    reducer.close()