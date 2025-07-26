document.addEventListener("DOMContentLoaded", () => {
    const tableRows = document.querySelectorAll("table tr");
    tableRows.forEach((row, index) => {
        if (index === 0){
            // ヘッダー行の設定はスキップする
            return;
        }

        row.addEventListener("mouseenter", (event) => {
            row.style.backgroundcolor = "#f0f8ff";
        });

        row.addEventListener("mouseleave", (event) => {
            row.style.backgroundcolor = "";
        });

        row.addEventListener("click", (event) => {
            alert("購入者：" + row.cells[0].innerText + "\n商品名：" + row.cells[2].innerText + "\n数量　：" + row.cells[4].innerText);
        });
    })
});