def make_action(file_name):
    action = open('actions/' + file_name + '.js', 'w')
    action.write("""
    export const BlankFunction = () => {
      return {
        type: 'SOME_STRING'
      };
    };

    """)
    action.close()
