
export default function Sim2() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <title>Simulation 2</title>
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        
        <div>
            <h1>World 2 Simulation</h1>
            <h2>Picking up large objects, the capabilities of robots.</h2>
            <video width="800" height="600" controls>
                <source src="\videos\vacuum_gripper.mp4" type="video/mp4"/>

                Your browser does not support the video tag.
            </video>
        </div>

        </main>
    </div>
  );
}
