inkling "2.0"
using Goal

# TODO: Change the SimConfig, SimState, and Action types to match the variables used in [SampleName].

type SimConfig {
    initial_value: number,
}

type SimState {
    value: number
}

type Action {
    addend: number<-10..10>
}

graph (input: SimState): Action {
    concept Concept(input): Action {
        curriculum {
            source simulator (Action: Action, Config: SimConfig): SimState {
            }

            training {
                EpisodeIterationLimit: 10
            }

            goal (state: SimState) {
                # TODO: Change the goal statement based on the objective that the [SampleName] will learn to achieve.
                reach Goal: state.value in Goal.Range(49.9, 50.1)
            }

            lesson `learn 1` {
                scenario { 
                    initial_value: number<0 .. 100>,
                }
            }
        }
    }
}
