
export default function Sim3() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <title>Simulation 3</title>
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        <div>
            <h1>World 3 Simulation</h1>
            <h2>The Tiago robot stirring a pot.</h2>
            {/* C:\Program Files\Webots\msys64\mingw64\bin\webotsw --stream[=port[=1236]] C:\Users\quinl\OneDrive\Documents\University Work\DissertationGit\wbots\worlds\Dissertation Stirring Tiago Complete.wbt*/}

            <video width="800" height="600" controls>
                <source src="\videos\Dissertation Stirring Tiago Complete.mp4" type="video/mp4"/>

                Your browser does not support the video tag.
            </video>
        </div>

        </main>
    </div>
  );
}
