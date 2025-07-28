'use strict'

let chart;

// 売上合計のグラフを表示させる
document.addEventListener("DOMContentLoaded", (event) => {
    const canvas = document.querySelector("#salesChart");
    if(!canvas){
        // 描写領域が存在しない場合は何もしない
        return;
    }

    const monthList = JSON.parse(document.querySelector("#months").textContent);
    const itemMonthValue = JSON.parse(document.querySelector("#item_sales_monthly").textContent);
    const dataset = itemMonthValue.map(item => ({
        label: item.item,
        data: item.month_value,
        borderWidth: 2,
        fill: false,
        tension: 0.3,
    }));

    const ctx = canvas.getContext("2d");
    chart = new Chart(ctx, {
        type: "line",
        data: {
            labels: monthList,
            datasets: dataset
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: "月別商品売上推移"
                },
                tooltip: {
                    callbacks: {
                        label: context => {
                            const value = context.parsed.y || 0;
                            return context.dataset.label + ": " + value.toLocaleString() + " 円";
                        }
                    }
                },
                legend: {
                    position: "bottom"
                }
            },
            scales: {
                y: {
                    ticks: {
                        callback: value => value.toLocaleString() + " 円"
                    }
                }
            }
        }
    });
});

// 商品名の表示・非表示ボタンの状態によって、グラフに当該商品データの表示・非表示を切り替える
document.addEventListener("DOMContentLoaded", (event) => {
    const isVisibleCheckBox = document.querySelectorAll(".is_visible");
    isVisibleCheckBox.forEach(checkBox => {
        checkBox.addEventListener("change", (event) => {
            const itemName = event.target.value;
            const isChecked = event.target.checked;

            const dataset = chart.data.datasets.find(ds => ds.label === itemName);
            if(dataset){
                dataset.hidden = !isChecked;
                chart.update();
            }
        });
    });
});