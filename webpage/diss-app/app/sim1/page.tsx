
export default function Sim1() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">

      <title>Simulation 1</title>

      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        <div>
            <h1>The robot, Panda, displaying picking up and placing food items.</h1>
            {/* webots --stream[=port[=1234]] C:\Users\quinl\OneDrive\Documents\University Work\DissertationGit\wbots\worlds\Dissertation Stirring Tiago Complete.wbt*/}

            <video width="800" height="600" controls>
                <source src="\videos\Dissertation Pick up and Place.mp4" type="video/mp4"/>

                Your browser does not support the video tag.
            </video>
            
        </div>

        </main>
    </div>
  );
}
